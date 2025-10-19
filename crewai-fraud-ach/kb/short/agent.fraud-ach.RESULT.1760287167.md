```json
{
  "id": "cb306d08f40ab2a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287167,
  "host_pid": "9e6742732c60:1",
  "hash": "f72dc40ad24483c44c2fe65ec5d10857db7a8b6f069c4003cb9016076d995a46",
  "cid": "QmV1f72dc40ad24483c44c2fe65ec5d10857db7a8b6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287167,
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
      "evaluated_at": 1760287167
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
  "sig": "9dfdae5e819a476058115f6fa2dcea1c52a214224a9fbc6c1c0c7bf2f444c9da"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 19262000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}