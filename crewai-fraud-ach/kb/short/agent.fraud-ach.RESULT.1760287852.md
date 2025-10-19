```json
{
  "id": "5c4fa19e85e288be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287852,
  "host_pid": "9e6742732c60:1",
  "hash": "0ac1cebaf4c4dae277e36148f11a113921f9ecd6f85adb5b37bba1751806771e",
  "cid": "QmV10ac1cebaf4c4dae277e36148f11a113921f9ecd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287852,
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
      "evaluated_at": 1760287852
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
  "sig": "844df01d9027630c33e9bcf6c370d4fa1874b48eea14a8b5f9a23758bd7a542c"
}
```

Fraud detected: round_amount_pattern (score: 74)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 74000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}