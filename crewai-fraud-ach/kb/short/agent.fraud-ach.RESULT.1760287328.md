```json
{
  "id": "4acbdcf129a4645d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287328,
  "host_pid": "9e6742732c60:1",
  "hash": "35ee6238cbfdd70900a488610cf1eb8cd3708290ed1eb6fbe347829abfa3fd09",
  "cid": "QmV135ee6238cbfdd70900a488610cf1eb8cd3708290",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287328,
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
      "evaluated_at": 1760287328
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
  "sig": "b39b03c713dcafcb065efd10fc2e20e6c2cb8e6d6e168647a55009c4ff0f1155"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 11287976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}