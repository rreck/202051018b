```json
{
  "id": "17af934a33515040",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286986,
  "host_pid": "9e6742732c60:1",
  "hash": "df995ee5b0815f0f9e4ab5b0e3aa6b30c64ec002a6e910493c72210d93cfa984",
  "cid": "QmV1df995ee5b0815f0f9e4ab5b0e3aa6b30c64ec002",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286986,
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
      "evaluated_at": 1760286986
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
  "sig": "b1e30db05198365a71cc196b2a7c5ff3388abad2a1941b5aad5682eef6d20300"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591273341
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '7aa2b4ab7394d79b'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}