```json
{
  "id": "44392d6fc99be708",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287842,
  "host_pid": "9e6742732c60:1",
  "hash": "e30522b0d49a5a6f762a3d67f965134e69541afeab04cfd7ea604961318ba2dc",
  "cid": "QmV1e30522b0d49a5a6f762a3d67f965134e69541afe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287842,
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
      "evaluated_at": 1760287843
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
  "sig": "555d48024d4d1da0ab6b490807f2cc1397d12bc1c67b83c5b823bca5dbd43c4a"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 026009592616863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285764, 'matching_hash': '1f69fcd8882944a6'}}}284979, 'matching_hash': 'a7542f9d69c5b02c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 5595688}}}