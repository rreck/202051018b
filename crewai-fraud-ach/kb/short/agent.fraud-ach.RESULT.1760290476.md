```json
{
  "id": "8fb6cb5c6c4d3c52",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290476,
  "host_pid": "9e6742732c60:1",
  "hash": "b9e66d2d3d8f7632e2076e27b7bf34304332747cb2094ad87d464e3001627e1d",
  "cid": "QmV1b9e66d2d3d8f7632e2076e27b7bf34304332747c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290476,
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
      "evaluated_at": 1760290476
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
  "sig": "e2e874383fc061c24d26f5fc56a3404234a45b1e6350b43323575f99abd85687"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 57525413, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}