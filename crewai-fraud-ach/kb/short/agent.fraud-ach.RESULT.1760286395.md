```json
{
  "id": "7ad953b8a41c0c76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286395,
  "host_pid": "9e6742732c60:1",
  "hash": "b9e0f7060758cb8cf4f15f15ee465511d3e04cc98eaa42137090656de3a76162",
  "cid": "QmV1b9e0f7060758cb8cf4f15f15ee465511d3e04cc9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286395,
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
      "evaluated_at": 1760286395
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
  "sig": "e535fa981d0fe32c1ecf784b4f8c19817dd57a5dda7abd7651c6555531c33892"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027732309
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '37acd6c3ead193e2'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}