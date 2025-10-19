```json
{
  "id": "7c2048488507bca4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287850,
  "host_pid": "9e6742732c60:1",
  "hash": "79abb612bb349855d93babeffe8c48eec50dd8c9dcc7ff95625bdefc9a628f64",
  "cid": "QmV179abb612bb349855d93babeffe8c48eec50dd8c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287850,
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
      "evaluated_at": 1760287850
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
  "sig": "bacd37edac45f713399aa6b659fa91a5a1b88673dd1464e9dd5420085c817bc6"
}
```

Fraud detected: round_amount_pattern (score: 74)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 74000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}