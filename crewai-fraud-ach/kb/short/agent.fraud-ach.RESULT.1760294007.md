```json
{
  "id": "d963f8455fd63586",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294007,
  "host_pid": "9e6742732c60:1",
  "hash": "c5ba45835453d4c4e0e181cdf416b6bdec0384ee151804b644186905a20a0c80",
  "cid": "QmV1c5ba45835453d4c4e0e181cdf416b6bdec0384ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294007,
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
      "evaluated_at": 1760294007
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
  "sig": "74296db6ae91462e41d303761c9cd1de441eeada65e691c04add0f1c5a8b425f"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 026009599754451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 1532789460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '546a5bdf8e1b6fa5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.38, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6664302}}}ils': {'pattern': 'exact_thousands', 'amount': 1000000}}}