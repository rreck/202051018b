```json
{
  "id": "a779946816d1d596",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289266,
  "host_pid": "9e6742732c60:1",
  "hash": "f1e143919d3575eecf98448eda8f90230e540caef6a9cbca9c599470c8ae4efc",
  "cid": "QmV1f1e143919d3575eecf98448eda8f90230e540cae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289266,
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
      "evaluated_at": 1760289266
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
  "sig": "8bf060cd7974b892a91e0bedc47aadd95a3bda1a2654cf051537b29bbf110041"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 121000242202372
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 1100147866, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '7eed822364ae6d91'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.9, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9323287}}}