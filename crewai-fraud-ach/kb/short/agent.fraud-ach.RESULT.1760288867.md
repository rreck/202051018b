```json
{
  "id": "4a76b53d7339904a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288867,
  "host_pid": "9e6742732c60:1",
  "hash": "560000990a70f202f6d5cd887787280ee48658a3540b8278a4dc6fadf2b1920a",
  "cid": "QmV1560000990a70f202f6d5cd887787280ee48658a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288867,
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
      "evaluated_at": 1760288867
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
  "sig": "37b2b3f3245b40639b1be7c49c524afe4d049da7637545f210c22a2e5098fa91"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 106000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}