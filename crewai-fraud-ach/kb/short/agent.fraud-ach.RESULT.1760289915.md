```json
{
  "id": "83caf321381a8f18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289915,
  "host_pid": "9e6742732c60:1",
  "hash": "c47e857a762bd3c4ac6776f8cf74b2ce8f05bee2505a36be2c47b4dd2bbd9ca3",
  "cid": "QmV1c47e857a762bd3c4ac6776f8cf74b2ce8f05bee2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289915,
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
      "evaluated_at": 1760289915
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
  "sig": "5e1fd1080461a654aa3db6b6730d16928438b07be404c41856ab810e37dbb5ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025375881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': '7f563b0766db4821'}}}