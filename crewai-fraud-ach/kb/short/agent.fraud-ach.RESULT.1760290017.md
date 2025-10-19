```json
{
  "id": "78941bced5839c1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290017,
  "host_pid": "9e6742732c60:1",
  "hash": "af43bb46aab6d8d091d71ccf55a2b9b39ad8e452a8539ad5de12d6c337f8296e",
  "cid": "QmV1af43bb46aab6d8d091d71ccf55a2b9b39ad8e452",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290017,
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
      "evaluated_at": 1760290017
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
  "sig": "5e55638229c9ea31f2b85fab5d6a7633f99cf273883b83f3045d5d3b2ea919dd"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105155421893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 703719053, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': 'b50b947262955843'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}