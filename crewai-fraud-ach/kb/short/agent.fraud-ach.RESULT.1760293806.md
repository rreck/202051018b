```json
{
  "id": "d99ee887f8de0943",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293806,
  "host_pid": "9e6742732c60:1",
  "hash": "afb5de5a58e5291fac6796a8422991723a6fbaecc0114745620453f021f768c4",
  "cid": "QmV1afb5de5a58e5291fac6796a8422991723a6fbaec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293806,
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
      "evaluated_at": 1760293806
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
  "sig": "8374a0ac77ec83204b830c942f2ecd7d1fc9052f001a9ba2c90bca15342a7b78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243793866
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 49160424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '3f378333472d9dcb'}}}