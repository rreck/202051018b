```json
{
  "id": "8c993f3d5dec6b23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294239,
  "host_pid": "9e6742732c60:1",
  "hash": "106f12a561983684701f8ad99bb305b60aa135cf9c23f24de383d7739944362e",
  "cid": "QmV1106f12a561983684701f8ad99bb305b60aa135cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294239,
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
      "evaluated_at": 1760294239
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
  "sig": "2d7154c33ac21e13b8746eced9c1b0768a7f747f6ad7f171d93da0e4d3531d87"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201460873764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 117000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '6dda2db9e90937c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}