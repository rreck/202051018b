```json
{
  "id": "9bb91cb1e0741584",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289868,
  "host_pid": "9e6742732c60:1",
  "hash": "4e18b43e6ee7db29ab32495ed867c916bf544dbe88cc79c6af8f09b7938dbd9f",
  "cid": "QmV14e18b43e6ee7db29ab32495ed867c916bf544dbe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289868,
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
      "evaluated_at": 1760289868
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
  "sig": "cfc1932735685bf0bfec77fa8f7864b17ca53fe7fa0bb80a3b3ca203ca5c6bae"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 1154153340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8549284}}}