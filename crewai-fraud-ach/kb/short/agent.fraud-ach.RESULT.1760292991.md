```json
{
  "id": "003ad50ddd3df536",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292991,
  "host_pid": "9e6742732c60:1",
  "hash": "9871458e4ee77351a372fc106d226f8339e375aa0b4452621623caba8f9ebf9c",
  "cid": "QmV19871458e4ee77351a372fc106d226f8339e375aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292991,
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
      "evaluated_at": 1760292991
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
  "sig": "59928ef374d7e04d9f0912a963eb52291d15fbfc45772bfbc85a6308ed12ea88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466969713
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 65018646, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '1e9180284a8352f5'}}}