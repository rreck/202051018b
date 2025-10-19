```json
{
  "id": "78cdb7b16a1912f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287761,
  "host_pid": "9e6742732c60:1",
  "hash": "1fd17b22f05d911cec1dc5405d5ebea3847bdd323a7f09614a592ce9787931ab",
  "cid": "QmV11fd17b22f05d911cec1dc5405d5ebea3847bdd32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287761,
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
      "evaluated_at": 1760287761
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
  "sig": "30fefc94980a0758f844e7619a07d4c70a3e48c60c2374d313fb54bd4fb46bd2"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 121000247383202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 28276105, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '32929947211460fd'}}}