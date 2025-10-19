```json
{
  "id": "40fe1333d5debf30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293043,
  "host_pid": "9e6742732c60:1",
  "hash": "e83cfddf96e95e748afc7a6f95d51fc97b92ef1bc5bc068b77df7d9a6e521313",
  "cid": "QmV1e83cfddf96e95e748afc7a6f95d51fc97b92ef1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293043,
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
      "evaluated_at": 1760293043
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
  "sig": "3b7e13f0adf8b4071e7c0fa8e902d881080bac4575e24e66f3adf78dd8393b6a"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 105000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}