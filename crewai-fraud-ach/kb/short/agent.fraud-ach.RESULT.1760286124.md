```json
{
  "id": "15d0e01ffadfff22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286124,
  "host_pid": "9e6742732c60:1",
  "hash": "78b8f4f11f0187cb90a6f0361907be0e449d4fc08924a959165b213f274c8ca5",
  "cid": "QmV178b8f4f11f0187cb90a6f0361907be0e449d4fc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286124,
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
      "evaluated_at": 1760286124
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
  "sig": "094a724a9132a93c716bc59143f315f0db628a40c31383dcbc8b53933ea54371"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461002751
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760284979, 'matching_hash': '0558b1bd8e64436c'}}}