```json
{
  "id": "276fc820ec0dbc86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293753,
  "host_pid": "9e6742732c60:1",
  "hash": "52cf1e24225a48a0bd312a157a1845ec46d776f0f36f1ceacc0f3d453b91bc56",
  "cid": "QmV152cf1e24225a48a0bd312a157a1845ec46d776f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293753,
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
      "evaluated_at": 1760293753
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
  "sig": "e6a90dfc715bac4e8db1781ad2ac2216fe0ddc5834b9d89f4fae47761f16359e"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000023922367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 1340192025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '420dc08dc8ad4808'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5956409}}}