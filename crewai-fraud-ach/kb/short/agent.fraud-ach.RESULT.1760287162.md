```json
{
  "id": "1ae4dcdf79f20fd6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287162,
  "host_pid": "9e6742732c60:1",
  "hash": "50d32a8e52362194f305d0d97a99c47d54b534f456d2968932c505ad3ab7229e",
  "cid": "QmV150d32a8e52362194f305d0d97a99c47d54b534f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287162,
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
      "evaluated_at": 1760287162
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
  "sig": "151c5835bc24d199879d4924473928692c655c2a75230a8767ee95539a99ebfa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 24102200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}