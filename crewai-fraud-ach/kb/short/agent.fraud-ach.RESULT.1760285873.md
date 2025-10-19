```json
{
  "id": "3aaf7b98bb015f91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285873,
  "host_pid": "9e6742732c60:1",
  "hash": "8e072405462d08989aa0d45b6cc205234da71f5a5a32d4a3249f1ad5a0543afb",
  "cid": "QmV18e072405462d08989aa0d45b6cc205234da71f5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285873,
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
      "evaluated_at": 1760285873
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
  "sig": "dea6e3e5d9671c1ae27946da4d66842c10d987a2691782034b51b682ed1dc11f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029265266
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 5, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}