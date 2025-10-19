```json
{
  "id": "7627bc17d7c34d79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290443,
  "host_pid": "9e6742732c60:1",
  "hash": "4cfa737dc58de8f4858d84ef1cf433e2d2369469207117936349bb8148168a80",
  "cid": "QmV14cfa737dc58de8f4858d84ef1cf433e2d2369469",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290443,
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
      "evaluated_at": 1760290443
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
  "sig": "05cb8452096e045c7fdb816ebe8e242a39ac919851d828e32b0c145eb6f3f77e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460708628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}