```json
{
  "id": "701fc39d9953b1b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290794,
  "host_pid": "9e6742732c60:1",
  "hash": "0625dbc538555de9c98349dfe5f05258eebd78115b3c5c9b11df461c01ae96cc",
  "cid": "QmV10625dbc538555de9c98349dfe5f05258eebd7811",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290794,
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
      "evaluated_at": 1760290794
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
  "sig": "66df62720b6942723decdae929cc7bcc8b5574177351608ff71ecfc16267c9b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 12227577, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}