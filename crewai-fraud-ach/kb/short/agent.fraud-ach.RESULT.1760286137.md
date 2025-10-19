```json
{
  "id": "36ac2ff42c41c783",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286137,
  "host_pid": "9e6742732c60:1",
  "hash": "ed1665a23643947a2a8f91262957c12148a886ccba499dca54514609e4377f97",
  "cid": "QmV1ed1665a23643947a2a8f91262957c12148a886cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286137,
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
      "evaluated_at": 1760286137
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
  "sig": "7cda1181fff474331237c3c7221a12bb0c4cbed36a630aa7af6d3fa2f272ba5c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}