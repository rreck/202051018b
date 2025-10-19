```json
{
  "id": "a1961ef33e1f6a1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286097,
  "host_pid": "9e6742732c60:1",
  "hash": "68256d003ef0818e8b9b755b9888d5615b7938013e996d5eb045b248a12b4594",
  "cid": "QmV168256d003ef0818e8b9b755b9888d5615b793801",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286097,
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
      "evaluated_at": 1760286097
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "a7db71d1f55521224ea5cf94a586b5b601f6a01f7bde43c3416999b158ce4855"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}