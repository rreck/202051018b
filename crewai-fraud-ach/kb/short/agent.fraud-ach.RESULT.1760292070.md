```json
{
  "id": "05843876c8683e9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292070,
  "host_pid": "9e6742732c60:1",
  "hash": "37457747c2c232bdb0a6734ef1fac8b43c8a338ca85e17ee06cee4b134223f68",
  "cid": "QmV137457747c2c232bdb0a6734ef1fac8b43c8a338c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292070,
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
      "evaluated_at": 1760292070
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
  "sig": "40fe499fc350c53f644284c8c900dd952a136be3946076019f21568df5962e32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021597485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 51000138, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '53d96e948794c738'}}}