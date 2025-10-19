```json
{
  "id": "faa12543967aa87d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286670,
  "host_pid": "9e6742732c60:1",
  "hash": "652ebd33ab1cee356ec003e80ca90460ad5cd71c6b97a7433f4fa298bad9634a",
  "cid": "QmV1652ebd33ab1cee356ec003e80ca90460ad5cd71c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286670,
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
      "evaluated_at": 1760286670
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
  "sig": "df5158598ca7faf3f5c8a784cb56cdcc52fd83828a3489cd87c52ddbd9dfb64a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245537248
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': '5bdcebee79eae34d'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760284979, 'matching_hash': '923cee7332714d41'}}}