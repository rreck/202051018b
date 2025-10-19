```json
{
  "id": "b3f30391c3cb8643",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292752,
  "host_pid": "9e6742732c60:1",
  "hash": "0eee01b648119da164963871a84fc28f2c193725d4bf91736529454929f17d0a",
  "cid": "QmV10eee01b648119da164963871a84fc28f2c193725",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292752,
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
      "evaluated_at": 1760292752
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
  "sig": "0eb2fe85bd4ace32ec0bf739336cf60dfca9fbb70b931f8d057a43cace32d80c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277678125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 65527248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': 'e82f6ac77d9f2ce9'}}}