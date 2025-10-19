```json
{
  "id": "ae2dc29b0eb96a3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287519,
  "host_pid": "9e6742732c60:1",
  "hash": "6406d6271070e42428cc13f15ef65cf7a04cd5daaf607a177966bef360cb0b39",
  "cid": "QmV16406d6271070e42428cc13f15ef65cf7a04cd5da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287519,
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
      "evaluated_at": 1760287519
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
  "sig": "066f0d5eb62bdcb96f65aed6d611b3cf782f42069237fc02807d4aed197c436b"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 026009591582850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 20826729, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '5102e2097242c74b'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}