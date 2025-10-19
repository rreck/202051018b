```json
{
  "id": "b22d157fa9e3d0f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292138,
  "host_pid": "9e6742732c60:1",
  "hash": "15595904422bbfbfedb27eaa070beccc02b45e178c12935a2eeca16831b47d4a",
  "cid": "QmV115595904422bbfbfedb27eaa070beccc02b45e17",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292138,
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
      "evaluated_at": 1760292138
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
  "sig": "5d13e9ec57df0ec37a55e975ef10452760bf024f389007ea57c0e009f4ab7d75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596829725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 63118624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '14fa64c7f7d5a53d'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8018325}}}