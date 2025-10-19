```json
{
  "id": "d6a253ed535f1b17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289357,
  "host_pid": "9e6742732c60:1",
  "hash": "b9ade4ac736b9f51d5f04c7570b9b025af5bee920ff91f113cd6dc3ef2db8d9d",
  "cid": "QmV1b9ade4ac736b9f51d5f04c7570b9b025af5bee92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289357,
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
      "evaluated_at": 1760289357
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
  "sig": "5d9dacbe68b018dbf72d7a0054c3c3107f6dafd74442f97ab8601376f2d8033e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154543608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285763, 'matching_hash': '3d9c367e54a48e12'}}}5763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9237211}}}