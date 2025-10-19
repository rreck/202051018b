```json
{
  "id": "433de72eb62f39fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293909,
  "host_pid": "9e6742732c60:1",
  "hash": "75e6cb4e1af3e59a6a9a1f70403ae96d12fa14e69db6b00d39262edfd26c04fc",
  "cid": "QmV175e6cb4e1af3e59a6a9a1f70403ae96d12fa14e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293909,
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
      "evaluated_at": 1760293909
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
  "sig": "ea2e3a402d1200f5ff6e6cc4ea0da7def8cfefaa5dc7a1267b800d7a89ec0549"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 122105150872647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1643735448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'f142eb53d77ea00a'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.69, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7209366}}}