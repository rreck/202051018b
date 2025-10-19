```json
{
  "id": "1a31337df983448b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291056,
  "host_pid": "9e6742732c60:1",
  "hash": "e405dafd15117092514cc2448eda62fcf011fe9b056666d13d11937cf4214543",
  "cid": "QmV1e405dafd15117092514cc2448eda62fcf011fe9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291056,
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
      "evaluated_at": 1760291056
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
  "sig": "7f7a6f72081811e61ee5777b6dd73bae171b9eb85a1f3be507bccf0a86a1cadf"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 026009595171446
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 1075420044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': '6f6a57bfd56698c7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6478434}}}