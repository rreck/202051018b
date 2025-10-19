```json
{
  "id": "1f68561711fc7152",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286258,
  "host_pid": "9e6742732c60:1",
  "hash": "422a968d0ab20f49cfe58a6559b77739f8b2748b6248d5ddd3f242e8b5212617",
  "cid": "QmV1422a968d0ab20f49cfe58a6559b77739f8b2748b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286258,
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
      "evaluated_at": 1760286258
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
  "sig": "c57e46053c371d53995a1fbfc38ea57f24386de9021ff3fb01775c42f0b0b5a5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}