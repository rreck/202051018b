```json
{
  "id": "d066a9e7e5d76f32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288306,
  "host_pid": "9e6742732c60:1",
  "hash": "e8ccff6d9271717e8ab663acd19b7bef00f880eea05bfdb3f260c086ce19c55d",
  "cid": "QmV1e8ccff6d9271717e8ab663acd19b7bef00f880ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288306,
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
      "evaluated_at": 1760288306
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "1354d4aa154230dd4a8cb8524254c4df17559db6eccf77d9e84771416d26322a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249337095
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 35405357, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': '2aad7fe43cc5d34d'}}}