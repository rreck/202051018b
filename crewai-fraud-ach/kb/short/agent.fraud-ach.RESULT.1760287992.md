```json
{
  "id": "6af4943be6c99ef9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287992,
  "host_pid": "9e6742732c60:1",
  "hash": "c569bbf51d2c83d669207a94614134bc87b477359e7ebfe7e9842b55ef9b6866",
  "cid": "QmV1c569bbf51d2c83d669207a94614134bc87b47735",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287992,
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
      "evaluated_at": 1760287992
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
  "sig": "2954212902741cf0b4646029a5e9ea6ab47ab8b455ffc2f30c3d85d1e20ab213"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031758687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 31897988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}