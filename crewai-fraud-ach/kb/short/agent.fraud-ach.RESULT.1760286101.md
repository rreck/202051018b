```json
{
  "id": "d4fff76cdb6e7b05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286101,
  "host_pid": "9e6742732c60:1",
  "hash": "fcb500e46ef345e747e7a5fc384bf4a9631888535f9263c043cc787982de3e63",
  "cid": "QmV1fcb500e46ef345e747e7a5fc384bf4a963188853",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286101,
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
      "evaluated_at": 1760286101
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
  "sig": "ebc49718bf48331718efea5cd5bee384111b92f9ce75ae99cb9af9666bfad2a3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009599118273
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285765, 'matching_hash': '777fe2ef7ab8cdc9'}}}