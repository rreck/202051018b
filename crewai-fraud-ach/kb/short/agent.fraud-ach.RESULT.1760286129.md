```json
{
  "id": "a2ce270a1885048e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286129,
  "host_pid": "9e6742732c60:1",
  "hash": "74ff44b99cc60ef6a91787e09138feb771b72b806b776d5fd9655eb95ae12b53",
  "cid": "QmV174ff44b99cc60ef6a91787e09138feb771b72b80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286129,
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
      "evaluated_at": 1760286129
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
  "sig": "09e6538b745793a71c1673dee3ff47953f766e370399102089dadc0be8a8c912"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105159548599
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285764, 'matching_hash': '3450667ce2814f1a'}}}