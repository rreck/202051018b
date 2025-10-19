```json
{
  "id": "c76b80d7fa84b238",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287815,
  "host_pid": "9e6742732c60:1",
  "hash": "25d9b3a80027babc9df4e00aa90fbb28777ad2dd8c2efe16882cd3cd878986e5",
  "cid": "QmV125d9b3a80027babc9df4e00aa90fbb28777ad2dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287815,
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
      "evaluated_at": 1760287815
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
  "sig": "47da3c86555eef1c932eb8d61b3805484a0eb6d18185fb3eb4654d5bd7c9a6ae"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}