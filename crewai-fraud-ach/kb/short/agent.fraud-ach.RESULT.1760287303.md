```json
{
  "id": "edd0588b451fa3a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287303,
  "host_pid": "9e6742732c60:1",
  "hash": "179e80c36038afe29f9c5a941f29389419d273107c51b7529c093785fd3247da",
  "cid": "QmV1179e80c36038afe29f9c5a941f29389419d27310",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287303,
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
      "evaluated_at": 1760287303
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
  "sig": "2d54c9ada5be340eb66ccdf94ae5d03605c86cf1d3a36fa66096c034a631dd46"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 10515285, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}