```json
{
  "id": "5945f4658fda7042",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286133,
  "host_pid": "9e6742732c60:1",
  "hash": "e990722234170fabcfffcb5a661b6259e25106b9770d3ea4ed321eca5fae6520",
  "cid": "QmV1e990722234170fabcfffcb5a661b6259e25106b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286133,
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
      "evaluated_at": 1760286133
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
  "sig": "9109bbdc2d23ca9bd6102b5ce4eaa7b8a91214b96b48c1ed8e54335798187d46"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593711033
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}