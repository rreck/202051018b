```json
{
  "id": "6c7ac078a29e29fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286613,
  "host_pid": "9e6742732c60:1",
  "hash": "a252086a4fc526056e2eca4f9760dc5a81d0e5b62e2ed28ab7c92ca791dcef1a",
  "cid": "QmV1a252086a4fc526056e2eca4f9760dc5a81d0e5b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286613,
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
      "evaluated_at": 1760286613
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
  "sig": "84b8c6c42a51de5530def381006c3c108ed36e9f82e618a7863e6c2acd2fa654"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279970164
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}