```json
{
  "id": "af184df11dcad188",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286068,
  "host_pid": "9e6742732c60:1",
  "hash": "5b66e5f543b24375455e0b925f1ba34065e0d2763f7c741c1c7fada2ce8cd27e",
  "cid": "QmV15b66e5f543b24375455e0b925f1ba34065e0d276",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286068,
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
      "evaluated_at": 1760286068
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
  "sig": "aea85166a842b10d4046be65df70898a2c1e0d8ff3c5cf8f5e8c214d346cfbb5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462125361
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285764, 'matching_hash': '410e2c6110d1d339'}}}