```json
{
  "id": "f74d0f8058216432",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293571,
  "host_pid": "9e6742732c60:1",
  "hash": "aa79998039bdfe56f83f334b25a6487bb5a3d7f64135234caf4ce79a3ce5a741",
  "cid": "QmV1aa79998039bdfe56f83f334b25a6487bb5a3d7f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293571,
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
      "evaluated_at": 1760293571
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
  "sig": "eef28ff59eaabad392e840395fb9cedf697aaa8cc4a46888645dfd000546b9fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 99677409, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}