```json
{
  "id": "d3e2cd19d6d8ef34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293588,
  "host_pid": "9e6742732c60:1",
  "hash": "f8f040f1db91697d8b9d421acf07c323a5ac3ad32347f6a5218686d114d3609d",
  "cid": "QmV1f8f040f1db91697d8b9d421acf07c323a5ac3ad3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293588,
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
      "evaluated_at": 1760293588
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
  "sig": "9743c8a3432a65fd16827ebc810edf383848ffd09f452a846125c73696079e8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 109090462, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}