```json
{
  "id": "487c5f0f64470021",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286566,
  "host_pid": "9e6742732c60:1",
  "hash": "8834a8b1dd3622c50432d678f95415e0da677985b09eb86f20055c9a7ff96e38",
  "cid": "QmV18834a8b1dd3622c50432d678f95415e0da677985",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286566,
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
      "evaluated_at": 1760286566
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
  "sig": "585d9819413b9cd5066a30dd6cc52baee1e2e7589085d6094e5c080e287d1a25"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}