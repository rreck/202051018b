```json
{
  "id": "a6f5e6176c12e4e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286370,
  "host_pid": "9e6742732c60:1",
  "hash": "8d790917cf7d799e15dee7dcb07fa618f2dae1f9f9cb9c042cda87158c811836",
  "cid": "QmV18d790917cf7d799e15dee7dcb07fa618f2dae1f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286370,
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
      "evaluated_at": 1760286370
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
  "sig": "5d53534acbcd2faf8ea5f420442bde041521a4b7bf794fa24046da08d0c58829"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245772760
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}