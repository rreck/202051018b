```json
{
  "id": "45e93a7b8847425d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292888,
  "host_pid": "9e6742732c60:1",
  "hash": "4317559464d8872a164a7741dd583dbd807a958ae8bc5e5a2568cadee0d249ba",
  "cid": "QmV14317559464d8872a164a7741dd583dbd807a958a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292888,
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
      "evaluated_at": 1760292888
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
  "sig": "b4cc1d644f0622def2c5a2267fb6b92f0b8321d8b6cdf683b421b2e59f08edbc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595535562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 27985779, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}