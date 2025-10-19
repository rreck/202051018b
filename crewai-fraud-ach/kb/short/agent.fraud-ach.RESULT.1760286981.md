```json
{
  "id": "71c1d140507bc6fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286981,
  "host_pid": "9e6742732c60:1",
  "hash": "a7f5d7f3c867f6cc8f265fd3f07ba15df48468d15a068e0169cae99bf228be23",
  "cid": "QmV1a7f5d7f3c867f6cc8f265fd3f07ba15df48468d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286981,
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
      "evaluated_at": 1760286981
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
  "sig": "a8760ba20966277b86cd6ebb2e7e02a448a97f923a8cd34a57cec1a58408cd02"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465723283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18811716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285764, 'matching_hash': 'e1350af409930159'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}