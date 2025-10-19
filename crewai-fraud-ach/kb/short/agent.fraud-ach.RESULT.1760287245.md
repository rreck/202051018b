```json
{
  "id": "879e8dd5282b2815",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287245,
  "host_pid": "9e6742732c60:1",
  "hash": "e97701257b9f2425a1263097b2b60c7cff78f69676676d4c0e376862852c9572",
  "cid": "QmV1e97701257b9f2425a1263097b2b60c7cff78f696",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287245,
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
      "evaluated_at": 1760287245
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
  "sig": "e24470404e41d3c933f31439934db4b313e8e098b6cf6f86f68b4a66ed43cfc5"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 044000036717829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285764, 'matching_hash': '49d069f76f563267'}}}