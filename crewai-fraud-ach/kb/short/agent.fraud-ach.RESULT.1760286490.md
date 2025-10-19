```json
{
  "id": "f76a9a3e301237bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286490,
  "host_pid": "9e6742732c60:1",
  "hash": "996886b6d627c54aedcd3c4f973e9e95374c908e8b78a24e32de5139185011cd",
  "cid": "QmV1996886b6d627c54aedcd3c4f973e9e95374c908e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286490,
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
      "evaluated_at": 1760286490
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
  "sig": "399d2f7d1d3d7323851b9c580f443dcf0d40f516a964e115d7fdb6caa31a867d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593654177
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285764, 'matching_hash': '5fbc310f1a1fe9dc'}}}