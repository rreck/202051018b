```json
{
  "id": "55aed231e24f23e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289329,
  "host_pid": "9e6742732c60:1",
  "hash": "82f0380a3a61a4a5470765e843aa7c9f24b0605190964bdb62405eab9a0acc3a",
  "cid": "QmV182f0380a3a61a4a5470765e843aa7c9f24b06051",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289329,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289329
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "74db621c20fdf1d2be2b5c2f8dcadd8c22437a446a9a42254c647a55e96d6b1a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 834096557545062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 40722000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285764, 'matching_hash': 'c4c3f7a3fe4b8b75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '834096558', 'validation_error': 'Invalid routing number checksum'}}}