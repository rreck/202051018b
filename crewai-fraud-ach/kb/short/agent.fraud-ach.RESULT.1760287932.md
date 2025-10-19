```json
{
  "id": "93c1b93f86976cb3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287932,
  "host_pid": "9e6742732c60:1",
  "hash": "abbaf5331ed2315055949ac85115f03e32894e1992c9e9cb5dead6872cba546e",
  "cid": "QmV1abbaf5331ed2315055949ac85115f03e32894e19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287932,
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
      "evaluated_at": 1760287932
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
  "sig": "9d816c99ab03cdc48df9d234c253ea35bd798e1ab0c5c9bf132483de9b0a776c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 044000032598305
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 472114181, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': '2af7a4570c2b815d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6131353}}}