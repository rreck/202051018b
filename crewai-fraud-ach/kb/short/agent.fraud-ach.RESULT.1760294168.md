```json
{
  "id": "b98f7d4c8080ec04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294168,
  "host_pid": "9e6742732c60:1",
  "hash": "7b2a337946ebe4eebbdd793803ff559c4f078435c59efe48dfd1cf7e2b20648d",
  "cid": "QmV17b2a337946ebe4eebbdd793803ff559c4f078435",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294168,
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
      "evaluated_at": 1760294169
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
  "sig": "dc854a7b1096232f7ac6921bade4c1b135fb9a5b52ae41363315ce59051a05ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026239341
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 98690878, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '200fd923cb07cfcf'}}}