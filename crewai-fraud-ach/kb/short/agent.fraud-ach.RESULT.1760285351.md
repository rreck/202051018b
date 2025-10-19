```json
{
  "id": "abe40dcf15f64710",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285351,
  "host_pid": "9e6742732c60:1",
  "hash": "47505520950d640897ca8d680c9eb1e7fa4023de039c91c3d3b9d2a09d5be7c7",
  "cid": "QmV147505520950d640897ca8d680c9eb1e7fa4023de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285351,
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
      "evaluated_at": 1760285351
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
  "sig": "257b13da11787727b709c0a1d50f7d62cbf3c0e6cff375d1506db05b433db5fb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15591578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}