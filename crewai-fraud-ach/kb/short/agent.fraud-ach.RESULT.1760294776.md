```json
{
  "id": "f0eea4679caab706",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294776,
  "host_pid": "9e6742732c60:1",
  "hash": "cc2779ec5722545ac60cab800f383ab0a515bece9206e4034fe7140f8d5068dd",
  "cid": "QmV1cc2779ec5722545ac60cab800f383ab0a515bece",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294776,
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
      "evaluated_at": 1760294777
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
  "sig": "54a7ed73eb94e6306e6af04568f4c46105a3ed3ed46779ba234c40a14ec76c07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461002751
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 82017184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}