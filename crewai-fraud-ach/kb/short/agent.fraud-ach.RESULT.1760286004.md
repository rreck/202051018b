```json
{
  "id": "a41ee63918a529ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286004,
  "host_pid": "9e6742732c60:1",
  "hash": "0eed73c6538ec52633354eaa8ceda9e2caa11b9eea68614b291bcb6123cdd281",
  "cid": "QmV10eed73c6538ec52633354eaa8ceda9e2caa11b9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286004,
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
      "evaluated_at": 1760286004
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
  "sig": "c74d45ec7f346ee32a2027ce43e5e4b8979e2494542d7e62498237acabf08060"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245537248
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '5bdcebee79eae34d'}}}