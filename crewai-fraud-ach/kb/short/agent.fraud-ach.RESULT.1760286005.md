```json
{
  "id": "c693f217e15e82bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286005,
  "host_pid": "9e6742732c60:1",
  "hash": "45d3438c6b1af25f216f62fcc24e578256a1d059b44cfadd87a0ad4aeedb87a8",
  "cid": "QmV145d3438c6b1af25f216f62fcc24e578256a1d059",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286005,
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
      "evaluated_at": 1760286005
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
  "sig": "7e799b1161946eaa8450403dfdcfe1698d6f7de110f106d66e2968f3905a55a8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000038959082
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '98ae9ae4174799d3'}}}