```json
{
  "id": "1f5b759ef7bbea21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286990,
  "host_pid": "9e6742732c60:1",
  "hash": "240f516c893640e79e15c81b2cd6dbda37e5aeea6ea0b9d2684b6b059a183404",
  "cid": "QmV1240f516c893640e79e15c81b2cd6dbda37e5aeea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286990,
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
      "evaluated_at": 1760286990
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
  "sig": "df45ad05ff8e874a54a4ad81bf668df16cca8e9f5d4d70b11c960fc453c7c27f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201469526930
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}