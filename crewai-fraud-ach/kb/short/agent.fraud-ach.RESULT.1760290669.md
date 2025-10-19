```json
{
  "id": "5603fc2f5f6fcca2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290669,
  "host_pid": "9e6742732c60:1",
  "hash": "2dbf3b769b79f955366b6a58b5a53fe313f414782d4b308adcab2bcc9d46e87f",
  "cid": "QmV12dbf3b769b79f955366b6a58b5a53fe313f41478",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290669,
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
      "evaluated_at": 1760290669
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
  "sig": "fd6d45bf7a216c8c9e81058b179df3fe7d3b55b00d470fb31b2b4f4e9f618eef"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105155421893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 789785412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': 'b50b947262955843'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}