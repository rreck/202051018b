```json
{
  "id": "97944f94ec498a2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286911,
  "host_pid": "9e6742732c60:1",
  "hash": "a1a72d18bb1c78b098dc5e5a052dbc34569f08d356fad924396db934b90e6700",
  "cid": "QmV1a1a72d18bb1c78b098dc5e5a052dbc34569f08d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286911,
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
      "evaluated_at": 1760286911
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
  "sig": "31e001f7615c0986f99da4e48e0e625a67eb8c2eb8c2d662e3937b5df4d54cf4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13048168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}