```json
{
  "id": "5fa8e99dc8ffffc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294279,
  "host_pid": "9e6742732c60:1",
  "hash": "f117dff828a7050646cca109797e6d168c430220936d5d3c983d1fd054946a94",
  "cid": "QmV1f117dff828a7050646cca109797e6d168c430220",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294279,
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
      "evaluated_at": 1760294280
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
  "sig": "1b1f2b0385d8d081fd336b44c6f737ef1d7dd482c652cdc12a043a2a594e3a26"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000240623413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 117500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285764, 'matching_hash': 'b41427cac750dd0e'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}