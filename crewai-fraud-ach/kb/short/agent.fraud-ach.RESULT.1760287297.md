```json
{
  "id": "fe64b7ffa72c9ce4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287297,
  "host_pid": "9e6742732c60:1",
  "hash": "86944f80667bf74e99b030630622897f990717a347be97fb5de44646a9df8d69",
  "cid": "QmV186944f80667bf74e99b030630622897f990717a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287297,
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
      "evaluated_at": 1760287297
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0db887811a83a9f66ef32243071a0c1eee2e281647f56fe7c17e85bc0ad5e531"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000034981344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 20888780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}