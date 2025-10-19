```json
{
  "id": "d766c68cb1ae8234",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289163,
  "host_pid": "9e6742732c60:1",
  "hash": "6deb4c0459c8840590d15e5c561bd5041a18744137d37a0f8a46df57f65c9919",
  "cid": "QmV16deb4c0459c8840590d15e5c561bd5041a187441",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289163,
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
      "evaluated_at": 1760289163
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
  "sig": "9cc0a370b951a0ec4f1f900f9c172c36bed61ca56daf08df35922d7f7bdfc5d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241083307
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 10506285, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': '06ddfe971a6a4d24'}}}