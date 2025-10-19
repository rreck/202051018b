```json
{
  "id": "e6a87798c5e3d938",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291961,
  "host_pid": "9e6742732c60:1",
  "hash": "1a50526b06be550cc73329d1b5470b772b229bc062e40954c310c27f8dae4e06",
  "cid": "QmV11a50526b06be550cc73329d1b5470b772b229bc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291961,
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
      "evaluated_at": 1760291962
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
  "sig": "1d70344647c2ea5fd550eea1cc99972c7bee87c36b8bdb8a8e94151b1cd09888"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273941483
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 58560920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '33ec4b85754ad38a'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8595712}}}