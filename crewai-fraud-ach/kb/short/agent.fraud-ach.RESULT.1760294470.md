```json
{
  "id": "3a02658b5f3afe53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294470,
  "host_pid": "9e6742732c60:1",
  "hash": "3546ceb867c8932f8fc60d7dfa12911f98a173ac3e047d5439aa611d5951e1e4",
  "cid": "QmV13546ceb867c8932f8fc60d7dfa12911f98a173ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294470,
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
      "evaluated_at": 1760294470
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
  "sig": "9ad0064995faa10e07ac33acfa80d8c2d7ab9523b7b74ed1ffad0554a3ad111d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 75743024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}