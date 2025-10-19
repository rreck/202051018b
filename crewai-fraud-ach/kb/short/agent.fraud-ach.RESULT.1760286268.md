```json
{
  "id": "8fc72ef8b7f46fff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286268,
  "host_pid": "9e6742732c60:1",
  "hash": "189c21002e7194ad7f2ddc79d590e9ba7b927a18b2fe2cef60146d33e6ead388",
  "cid": "QmV1189c21002e7194ad7f2ddc79d590e9ba7b927a18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286268,
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
      "evaluated_at": 1760286268
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
  "sig": "b1ee5ced59ffa3a8df18189d44396f8381bb7ba3f0b17e35c627e20949fd4710"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026803563
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}