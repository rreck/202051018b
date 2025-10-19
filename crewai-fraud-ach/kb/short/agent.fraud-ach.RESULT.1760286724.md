```json
{
  "id": "1a9ff2328b890cca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286724,
  "host_pid": "9e6742732c60:1",
  "hash": "bf027b30596a19d25ba815a1cf135078080e3d816a0047738c4b278ba1e5f15a",
  "cid": "QmV1bf027b30596a19d25ba815a1cf135078080e3d81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286724,
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
      "evaluated_at": 1760286724
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
  "sig": "66f91a4a23875dd63480ff7fed1395c07bbeb26820fc65d31145b703e75cb09f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240515775
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}