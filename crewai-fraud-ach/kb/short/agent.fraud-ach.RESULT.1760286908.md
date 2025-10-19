```json
{
  "id": "2248809ae273abd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286908,
  "host_pid": "9e6742732c60:1",
  "hash": "56dd7a5871610004c1d054e1d49250c3c6af32e9ad1c4a617598da9e97012241",
  "cid": "QmV156dd7a5871610004c1d054e1d49250c3c6af32e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286908,
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
      "evaluated_at": 1760286908
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
  "sig": "9d44f4337089801f950de154451972e66e70988730e270a5fe72458cfe2af8c2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13711548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}