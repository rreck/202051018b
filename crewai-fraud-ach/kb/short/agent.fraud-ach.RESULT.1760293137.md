```json
{
  "id": "c8e7179fba901829",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293137,
  "host_pid": "9e6742732c60:1",
  "hash": "c4d6446a0fc81a562d31d23e00424db9a042eedf3241666644232711ab2a8cd3",
  "cid": "QmV1c4d6446a0fc81a562d31d23e00424db9a042eedf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293137,
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
      "evaluated_at": 1760293137
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
  "sig": "20a2afb3d63929759a7ee99f25c20b7fb0cd25084b695e57f40477ea9f8679c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 76495112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}