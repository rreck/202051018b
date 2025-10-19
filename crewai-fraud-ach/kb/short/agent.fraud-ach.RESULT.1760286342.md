```json
{
  "id": "106b9152ce108f9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286342,
  "host_pid": "9e6742732c60:1",
  "hash": "f1987e20cae33c6bd0b57a38489fbc226e8987885b5c7873f115b6f0924e7afa",
  "cid": "QmV1f1987e20cae33c6bd0b57a38489fbc226e898788",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286342,
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
      "evaluated_at": 1760286342
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
  "sig": "cb1848acb360c006d1cd508ac79ce6f28bc327f0b6539c718dffc2aecfea2ac9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000246033311
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10557140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285764, 'matching_hash': 'd9b4b01f0add79d3'}}}