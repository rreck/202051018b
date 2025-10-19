```json
{
  "id": "3c8bec101dcd3dff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289949,
  "host_pid": "9e6742732c60:1",
  "hash": "d59063710c45253b753686e14122c33bdac252a16b0aa2f922672f3973711b5e",
  "cid": "QmV1d59063710c45253b753686e14122c33bdac252a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289949,
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
      "evaluated_at": 1760289949
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
  "sig": "c98e337c657ff892c6f078b05fc8c14675f018e029187d80a9e7770d205e6654"
}
```

Fraud detected: amount_anomaly (score: 87)
Transaction: 063100278543685
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 971242046, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': 'e9470cd0cc07fb40'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 76, 'details': {'zscore': 3.62, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7089358}}}