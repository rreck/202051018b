```json
{
  "id": "08eb61449e281e91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294550,
  "host_pid": "9e6742732c60:1",
  "hash": "6e1efd2d213ef1977b31646b767ab0c3df0420ed3b253bf668ed94cd749f93e5",
  "cid": "QmV16e1efd2d213ef1977b31646b767ab0c3df0420ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294550,
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
      "evaluated_at": 1760294550
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
  "sig": "2343e2b636368369ad2994c2bf2cff414b087c380d104b4dc9bed756127600e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 22470240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}