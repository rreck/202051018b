```json
{
  "id": "adc6776de40178bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285939,
  "host_pid": "9e6742732c60:1",
  "hash": "02a0a3e47f2cfd0e945b49f017152bdf03035cc81498469e28f0ff7fb5c52f99",
  "cid": "QmV102a0a3e47f2cfd0e945b49f017152bdf03035cc8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285939,
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
      "evaluated_at": 1760285939
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
  "sig": "8f1ef70ca83af43d50e7935dba82305373e9e29990801701d7ee95889c8e73b4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105157097598
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '62fa124f01b3075a'}}}