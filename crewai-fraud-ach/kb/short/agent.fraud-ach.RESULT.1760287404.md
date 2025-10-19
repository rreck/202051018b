```json
{
  "id": "48d542eb7f35bd15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287404,
  "host_pid": "9e6742732c60:1",
  "hash": "ec54afc07fb20dee7cfeecfbb33afe04c20f21b8605f222ea7188418e242345c",
  "cid": "QmV1ec54afc07fb20dee7cfeecfbb33afe04c20f21b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287404,
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
      "evaluated_at": 1760287404
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
  "sig": "02f555af864d4665e4655ed94bf920a44de30abf4184c7e3074c4c4c62a13573"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 063100277592839
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 59000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': 'd907a2a28cc997b7'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}mount': 7854285}}}