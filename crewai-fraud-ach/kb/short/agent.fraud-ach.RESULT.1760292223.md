```json
{
  "id": "4513a9d39ee0f5a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292223,
  "host_pid": "9e6742732c60:1",
  "hash": "59e4b6cc53ead0730e04ddef4935e42f212cb3130321f220cdf4ab9a7840a819",
  "cid": "QmV159e4b6cc53ead0730e04ddef4935e42f212cb313",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292223,
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
      "evaluated_at": 1760292223
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
  "sig": "7366f66d4faccb40c6fd7207374d723e56e86c29f79c5022a08fc3ce8478ebb2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362528
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 82502675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '85f76e3ae9d0eff6'}}}