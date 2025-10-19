```json
{
  "id": "df94400ed9fd1012",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287022,
  "host_pid": "9e6742732c60:1",
  "hash": "10c755a3af6c28025d48035d4bc8830ee8b6e07b8b4e03b67a5f6708ef3bcf79",
  "cid": "QmV110c755a3af6c28025d48035d4bc8830ee8b6e07b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287022,
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
      "evaluated_at": 1760287022
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "148fa077ad5853ee57d1566a1cc81dee2236c9d4eaee55aafea4759000fbbd96"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11193210, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}