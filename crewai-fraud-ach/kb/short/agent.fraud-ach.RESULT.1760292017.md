```json
{
  "id": "9a53b21c481d9833",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292017,
  "host_pid": "9e6742732c60:1",
  "hash": "b1bdca75e8a8f22db737765faea2d4e37b80055e095808975c9e3561d0392add",
  "cid": "QmV1b1bdca75e8a8f22db737765faea2d4e37b80055e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292017,
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
      "evaluated_at": 1760292017
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "c58391139f3c9972aaabd775ce5b5021cab45d67b7339683268434097e8b0afb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597785743
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': 'c11d2019f761950d'}}} 1760285763, 'matching_hash': 'ac12af19574e93c9'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}