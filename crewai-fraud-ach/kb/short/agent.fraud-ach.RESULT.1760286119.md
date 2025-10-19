```json
{
  "id": "aacaf95264c9c2cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286119,
  "host_pid": "9e6742732c60:1",
  "hash": "e01b75c17042a23dce446bf33f0ab69e611bc82315a0d05dee5ee24ce6d4c969",
  "cid": "QmV1e01b75c17042a23dce446bf33f0ab69e611bc823",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286119,
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
      "evaluated_at": 1760286119
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
  "sig": "6d33681c18a8b7aa63cf099cc0c410a50142ff88782fb75a12db046584bf49ed"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027294403
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}