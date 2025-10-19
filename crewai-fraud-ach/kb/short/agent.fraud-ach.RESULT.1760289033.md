```json
{
  "id": "027df9d7a1bf4c6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289033,
  "host_pid": "9e6742732c60:1",
  "hash": "cdd1e0dff33794252d7bfaec4c28e20d429cad80e9b14b3df9bc69d2649b847a",
  "cid": "QmV1cdd1e0dff33794252d7bfaec4c28e20d429cad80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289033,
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
      "evaluated_at": 1760289033
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
  "sig": "851cf1463111df557a821eed96e0c219b09fa179538c7050fab90ae15471db7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467007138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 46586034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': '0c635cab5f5b8acd'}}}