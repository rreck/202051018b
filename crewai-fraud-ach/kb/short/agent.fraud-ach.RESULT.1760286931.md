```json
{
  "id": "8066087a6eee6531",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286931,
  "host_pid": "9e6742732c60:1",
  "hash": "6b798104717a1216ad5b156643d8060809bdc0f45452c0a8a398855bfb254a6a",
  "cid": "QmV16b798104717a1216ad5b156643d8060809bdc0f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286931,
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
      "evaluated_at": 1760286931
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
  "sig": "f07db0ddde9e903dc1c0adcfe93167a1f6d456f3d5cc8b7651560865246629bc"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 42000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}