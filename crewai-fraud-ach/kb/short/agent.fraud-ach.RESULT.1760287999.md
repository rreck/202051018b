```json
{
  "id": "9796a89bd77bbbf9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287999,
  "host_pid": "9e6742732c60:1",
  "hash": "74d3e088ed9b458c6cc7fef2b4e6f0589bdc42810fb58845bdc453ff10480b5f",
  "cid": "QmV174d3e088ed9b458c6cc7fef2b4e6f0589bdc4281",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287999,
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
      "evaluated_at": 1760287999
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
  "sig": "a105f6bdf09b5aa893deda42f246a463638e07bacd77d2a2288ec4287896c2fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464170386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285764, 'matching_hash': 'cc3f2cd033134006'}}}