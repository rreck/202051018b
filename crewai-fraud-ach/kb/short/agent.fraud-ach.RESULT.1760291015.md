```json
{
  "id": "194cf8fb712f3208",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291015,
  "host_pid": "9e6742732c60:1",
  "hash": "6a1147fa9b6046e1a55b0a5267b37d91fa4413b6f70d1fa91c15e9cc2b47a379",
  "cid": "QmV16a1147fa9b6046e1a55b0a5267b37d91fa4413b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291015,
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
      "evaluated_at": 1760291015
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
  "sig": "f0685b4a90866f09d2dd9c37da7698e7b94dacc4cb7d02de2b5d84faed22e791"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244096993316032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 42877560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}