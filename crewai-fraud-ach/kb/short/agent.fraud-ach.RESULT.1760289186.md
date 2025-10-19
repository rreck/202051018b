```json
{
  "id": "fac609618b9ed19e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289186,
  "host_pid": "9e6742732c60:1",
  "hash": "008cdbf5a2c415a1c09c56b5e6c4ebe1cd84af2f7b6ab0ec7fa8667503f41ab5",
  "cid": "QmV1008cdbf5a2c415a1c09c56b5e6c4ebe1cd84af2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289186,
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
      "evaluated_at": 1760289186
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
  "sig": "db0419196411dbbb845ef4e55605cd2f8df87c12a9c0d2ea12518d8d7c6fe637"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029303857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 30314744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '4510d576292a5401'}}}