```json
{
  "id": "6adc91ad2e3f4586",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287488,
  "host_pid": "9e6742732c60:1",
  "hash": "562167d5441f363733864cc98ad5772c696cc75ce13c0d669d8928ebee7bbc53",
  "cid": "QmV1562167d5441f363733864cc98ad5772c696cc75c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287488,
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
      "evaluated_at": 1760287488
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
  "sig": "60237c6ac2663bcfec9867d36a63dac71fcf58bc5fc5343a1668cac2d415e50d"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 063100278849424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 17761698, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}