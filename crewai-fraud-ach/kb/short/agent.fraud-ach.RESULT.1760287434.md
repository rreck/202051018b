```json
{
  "id": "a211f83c2ecbdac5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287434,
  "host_pid": "9e6742732c60:1",
  "hash": "ac1814ba1c8cf7cde1f7c9153f962152fdd8e2531c3d22c27992bc30f1e15444",
  "cid": "QmV1ac1814ba1c8cf7cde1f7c9153f962152fdd8e253",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287434,
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
      "evaluated_at": 1760287434
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
  "sig": "56595b22675daa0b985345026bac9813c2873c4da6f2cc60d7e08e9c3c406a07"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021412484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 14755800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285764, 'matching_hash': 'a5f4ca8ac1007b12'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6602570}}}