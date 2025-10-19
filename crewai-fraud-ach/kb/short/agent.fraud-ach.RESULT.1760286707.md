```json
{
  "id": "54fb2fb9a8d2e01e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286707,
  "host_pid": "9e6742732c60:1",
  "hash": "36a9299ebdeb06a544e08aa362cb529138e8913d781e17cd603d2dfd53659388",
  "cid": "QmV136a9299ebdeb06a544e08aa362cb529138e8913d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286707,
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
      "evaluated_at": 1760286707
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
  "sig": "341071235bf40b9bd7b5d843f5e4d263895c86d93cbf2cd20134283127e6c42e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243970709
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}