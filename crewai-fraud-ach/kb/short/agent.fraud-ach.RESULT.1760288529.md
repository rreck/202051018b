```json
{
  "id": "a3a9346d6f9c17d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288529,
  "host_pid": "9e6742732c60:1",
  "hash": "ffd48d000722363851d41286eeaffa1f49b7b0d1bdbe5fbdddf5d513eac9325f",
  "cid": "QmV1ffd48d000722363851d41286eeaffa1f49b7b0d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288529,
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
      "evaluated_at": 1760288529
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
  "sig": "7ce91951f9528d3aa7b8002c16efc333b22e630dba18d779d080daac4b427642"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 34631424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}