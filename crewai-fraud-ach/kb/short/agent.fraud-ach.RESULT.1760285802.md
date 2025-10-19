```json
{
  "id": "fa2e9767385db2ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285802,
  "host_pid": "9e6742732c60:1",
  "hash": "3a75860f33b0b4c9169e937ac35d0edd50db33fae64acb125ed214dbe0e3194c",
  "cid": "QmV13a75860f33b0b4c9169e937ac35d0edd50db33fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285802,
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
      "evaluated_at": 1760285802
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
  "sig": "e32199332bb7a2b5fa0a9abeeb42f1965a95587131cb84eadf13853003d54abf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154971432
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285764, 'matching_hash': 'db584ac34c85fc07'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}