```json
{
  "id": "60fa25cbb66dc5a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286273,
  "host_pid": "9e6742732c60:1",
  "hash": "0603abd1f8d6d71f2b2d6c6a876fd8821f4eb1774e2797223eb0671cb8e4b89c",
  "cid": "QmV10603abd1f8d6d71f2b2d6c6a876fd8821f4eb177",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286273,
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
      "evaluated_at": 1760286273
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
  "sig": "fb3d0f9f63a23b9af92431e6a60a9af7c675c888d9ca7c5aa56ab2e16b40a02b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598551005
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285764, 'matching_hash': 'f05e3d2f96782052'}}}