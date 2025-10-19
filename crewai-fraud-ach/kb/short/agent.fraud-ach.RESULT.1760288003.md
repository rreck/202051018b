```json
{
  "id": "a9e86aec9bc1c00e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288003,
  "host_pid": "9e6742732c60:1",
  "hash": "24b495a5fd4d821959bc0f5ab3774a810a1eadb134db3e09e4df71085adc85ed",
  "cid": "QmV124b495a5fd4d821959bc0f5ab3774a810a1eadb1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288003,
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
      "evaluated_at": 1760288003
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
  "sig": "cf7f3a2ad231f0a13780318925ab1deb2c42637c34c3033c32e1478f1728e41c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153543170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}