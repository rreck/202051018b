```json
{
  "id": "c92622872901536e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286092,
  "host_pid": "9e6742732c60:1",
  "hash": "b91343b7aa3abd86f78d60a4cbbf6bb81eef9394654dc372cc4d19d839f8348c",
  "cid": "QmV1b91343b7aa3abd86f78d60a4cbbf6bb81eef9394",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286092,
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
      "evaluated_at": 1760286092
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
  "sig": "77e3f1518cde815ce1e1f8335a2828059f20c9782962c9625c78b4f9708b7485"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467394934
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '227a4380e23ca7de'}}}