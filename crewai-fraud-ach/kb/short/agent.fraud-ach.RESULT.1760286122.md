```json
{
  "id": "5c9ef52905d82b37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286122,
  "host_pid": "9e6742732c60:1",
  "hash": "df931eec680c08738d18bfdb42287deb695f581f62bcd3f9d335b8432f600cac",
  "cid": "QmV1df931eec680c08738d18bfdb42287deb695f581f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286122,
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
      "evaluated_at": 1760286122
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
  "sig": "d5c9bff1a736da8a64195f1f24ab3b2beb0a6bb168e57c0dcfe71db77ef734d5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020376030
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}