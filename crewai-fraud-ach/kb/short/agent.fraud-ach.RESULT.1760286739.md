```json
{
  "id": "3ba2a5bbd9ad548d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286739,
  "host_pid": "9e6742732c60:1",
  "hash": "5501c971ee985711032a6348517f7bdf0386a4f0e6f4004000008f01fbadecf1",
  "cid": "QmV15501c971ee985711032a6348517f7bdf0386a4f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286739,
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
      "evaluated_at": 1760286739
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
  "sig": "9c40a60eef8f14f732e2be3e1993950440a95a1d054106753c892ba126dbe2b2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039867307
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '2a6987d2199b8b86'}}}