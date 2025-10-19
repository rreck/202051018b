```json
{
  "id": "3d1dc762e1cb4f7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291713,
  "host_pid": "9e6742732c60:1",
  "hash": "8fd22034b9b5152c086d4d74132c0c44a2b143165b30669176619c9e2ea9fdd0",
  "cid": "QmV18fd22034b9b5152c086d4d74132c0c44a2b14316",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291713,
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
      "evaluated_at": 1760291713
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
  "sig": "f533a90ed58f7b93817ae06da336f1b8c0c9deff3730ece1f20f368fcd5d1208"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 30699591, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}