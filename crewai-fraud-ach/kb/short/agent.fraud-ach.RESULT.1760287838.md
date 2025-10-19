```json
{
  "id": "c3eb6f68485ee7db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287838,
  "host_pid": "9e6742732c60:1",
  "hash": "71a095784e8bb9cbe02d9b3eb52bd51b9c3bc7b1f81cfb9826299c40384510a1",
  "cid": "QmV171a095784e8bb9cbe02d9b3eb52bd51b9c3bc7b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287838,
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
      "evaluated_at": 1760287838
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
  "sig": "595bc24594a1793cf8ec7e70c8416dfb3a1ff515fafdff5cd4faa4ee30caaf96"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}