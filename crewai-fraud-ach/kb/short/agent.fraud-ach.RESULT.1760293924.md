```json
{
  "id": "aafc8143ddb26daa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293924,
  "host_pid": "9e6742732c60:1",
  "hash": "400cc522230f4ba238c1f6f5b0c3f085b956bebe99c52cd075ccb2695b322aab",
  "cid": "QmV1400cc522230f4ba238c1f6f5b0c3f085b956bebe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293924,
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
      "evaluated_at": 1760293924
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "7aaade203363cb7ee6e050f5c2267aecc758213ffb37c8671a4ed72991770da0"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275692414
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1256989764, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': '9e6182bea86cf2e1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5513113}}}