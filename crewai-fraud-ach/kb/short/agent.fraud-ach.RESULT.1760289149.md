```json
{
  "id": "652b47c9bbc1c069",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289149,
  "host_pid": "9e6742732c60:1",
  "hash": "dc0cf294e1997c0e5d86637c897287f3308d6d7838da4f1787d6d3a867f69538",
  "cid": "QmV1dc0cf294e1997c0e5d86637c897287f3308d6d78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289149,
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
      "evaluated_at": 1760289149
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
  "sig": "9f8a433277ef98bed1601a7c585fb23fd6302bcfcb636322b382083c0e63f58d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465006650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 20989685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': 'ac98f3afdd973e27'}}}