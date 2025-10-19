```json
{
  "id": "dfc390e760f84327",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290870,
  "host_pid": "9e6742732c60:1",
  "hash": "8d2f12bf1074b3034688b7cc424d80c70c0d8e2ec13e98b41089a6d352988edb",
  "cid": "QmV18d2f12bf1074b3034688b7cc424d80c70c0d8e2e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290870,
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
      "evaluated_at": 1760290870
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
  "sig": "02643bd73aaa8e326d15a2b5f3384cd7700fa5ba25ce14bf661a7c7b50840f1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270534223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 28846048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '6dd341e8ae885101'}}}