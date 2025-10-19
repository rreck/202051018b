```json
{
  "id": "73d0bc685145cf9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287458,
  "host_pid": "9e6742732c60:1",
  "hash": "2da40455c17260fc46315df3d3ba35943b7ef6b49265a31cf45e3ef7e5f1001e",
  "cid": "QmV12da40455c17260fc46315df3d3ba35943b7ef6b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287458,
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
      "evaluated_at": 1760287458
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8e4af0aa7ebef79a06c1fb088b172f22536cb4e5c26d5e9a6ea4df62a8b4984c"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 13377361, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}