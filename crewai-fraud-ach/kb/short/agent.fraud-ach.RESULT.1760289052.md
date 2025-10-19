```json
{
  "id": "b84d3f5a1992d809",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289052,
  "host_pid": "9e6742732c60:1",
  "hash": "08aa71d4637ccb77cee425c56d5e27824c196458f29e71581bb0b48b8d06a8cb",
  "cid": "QmV108aa71d4637ccb77cee425c56d5e27824c196458",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289052,
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
      "evaluated_at": 1760289052
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
  "sig": "33c5527bc4f81af1b9ae174d62cc2964a7d8a2fbe68a500c551528224b448d8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020947870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}