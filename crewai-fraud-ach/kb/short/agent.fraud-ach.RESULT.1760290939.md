```json
{
  "id": "65acea1cc4fc4eb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290939,
  "host_pid": "9e6742732c60:1",
  "hash": "c5892a056fdbaac6bc9844691d1991bb30aa580d773e9e1fb88664329b196dea",
  "cid": "QmV1c5892a056fdbaac6bc9844691d1991bb30aa580d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290939,
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
      "evaluated_at": 1760290939
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
  "sig": "4503d10486643fe130448358f3a7a2b17d18866f9e715a5bdfd63e0a8d47271b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023603818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 73191238, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285764, 'matching_hash': '07334b550f79eb68'}}}