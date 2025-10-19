```json
{
  "id": "66ee1fcffe4dea00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287895,
  "host_pid": "9e6742732c60:1",
  "hash": "cd8aeeb6741780c0dcdd3ff8f4236860697587dc679534fcd05a7af631f56dd1",
  "cid": "QmV1cd8aeeb6741780c0dcdd3ff8f4236860697587dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287895,
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
      "evaluated_at": 1760287895
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
  "sig": "088351ed68f9f256a8e01f49d430fb8568f6486fa0983e16375b0b67b2a3df86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035823466
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 33186160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7623976}}}