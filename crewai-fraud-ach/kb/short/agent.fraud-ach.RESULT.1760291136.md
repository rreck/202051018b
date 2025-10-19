```json
{
  "id": "5e6dfe825c5e0fce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291136,
  "host_pid": "9e6742732c60:1",
  "hash": "4a299cee3017652d13cfcd5798ff62f861c3f1cfe6a05bbbc4e9db909b394d9c",
  "cid": "QmV14a299cee3017652d13cfcd5798ff62f861c3f1cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291136,
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
      "evaluated_at": 1760291136
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
  "sig": "724c78767080741fb45518b50cf901fa16c2d33661f8330c336dc342773d09d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038823890
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 35102088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '81df70e06ca09887'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}