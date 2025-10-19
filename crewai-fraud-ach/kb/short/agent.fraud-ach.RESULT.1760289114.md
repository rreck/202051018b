```json
{
  "id": "7a89d338ef525c89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289114,
  "host_pid": "9e6742732c60:1",
  "hash": "bf72396ee6c8091780b0c27937e5d2cb27577fa3ba6383c1830a2591dd1432b1",
  "cid": "QmV1bf72396ee6c8091780b0c27937e5d2cb27577fa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289114,
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
      "evaluated_at": 1760289114
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
  "sig": "7f1e00b1df33e089b1237881096792c3874df90c55ce3f861d1c987588aa55ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595856880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 35647002, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': '3e252270c9e333bc'}}}