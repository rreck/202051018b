```json
{
  "id": "9c1a273e5efadeb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286367,
  "host_pid": "9e6742732c60:1",
  "hash": "ca10a55db551094adefb56962eec4df0c08945967fa5e7ceb5f6e3aad66d793c",
  "cid": "QmV1ca10a55db551094adefb56962eec4df0c0894596",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286367,
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
      "evaluated_at": 1760286367
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
  "sig": "20c566f80cc6eeff3c47f1663d6e118b8a13cdad8ec7aa9ef1372eb098075025"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031758687
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '8a33e153fff23185'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '1f36f93e880b57ba'}}}