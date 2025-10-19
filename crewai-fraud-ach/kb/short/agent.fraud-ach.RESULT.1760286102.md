```json
{
  "id": "07be17d2f86b100c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286102,
  "host_pid": "9e6742732c60:1",
  "hash": "98074dacb4405ade9676abcfb990e54d045f41015a4394f84a7c5928c494e2b4",
  "cid": "QmV198074dacb4405ade9676abcfb990e54d045f4101",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286102,
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
      "evaluated_at": 1760286102
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
  "sig": "464d72792bd9c6a608569966df54077ffdd90f81130e195071d687f46af1cdd8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000033751291
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}