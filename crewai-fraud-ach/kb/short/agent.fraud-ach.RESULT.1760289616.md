```json
{
  "id": "f11cad5acb1d5722",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289616,
  "host_pid": "9e6742732c60:1",
  "hash": "044ccb1be21a357e87d2cc31ac837258614550a309cf55ca1b604ec9726c8f57",
  "cid": "QmV1044ccb1be21a357e87d2cc31ac837258614550a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289616,
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
      "evaluated_at": 1760289616
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
  "sig": "c152347bd5d55f6e9727cc54a40406d40e6838b7438e82c97d6b6f0b330acfab"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 128000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}