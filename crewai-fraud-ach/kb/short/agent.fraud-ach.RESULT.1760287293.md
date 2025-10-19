```json
{
  "id": "d607235c1df4d316",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287293,
  "host_pid": "9e6742732c60:1",
  "hash": "012efa04bde098f717fbfb1d5874ad58fa921ed4a003407aaa286f37befaa71a",
  "cid": "QmV1012efa04bde098f717fbfb1d5874ad58fa921ed4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287293,
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
      "evaluated_at": 1760287293
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
  "sig": "ce9fe484ef1d5dbe2aa614342db5d68d2716ecdf6a739c136ce9e14454d4679e"
}
```

Fraud detected: duplicate_transaction (score: 72)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 60, 'details': {'transaction_count': 55, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}een': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}