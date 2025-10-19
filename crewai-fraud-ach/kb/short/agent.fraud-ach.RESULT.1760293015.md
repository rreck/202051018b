```json
{
  "id": "64cc5eb262505edd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293015,
  "host_pid": "9e6742732c60:1",
  "hash": "1b104e20e3a11ee6049080e5b768e81308aa81d5075a53c38f6df97889fb01d9",
  "cid": "QmV11b104e20e3a11ee6049080e5b768e81308aa81d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293015,
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
      "evaluated_at": 1760293015
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
  "sig": "015b5a08e87b00bd14fc75c944d45efc39776ce7d70688e13468da274bd5dd01"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463734572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 105000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '9877b0a7b07093eb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}