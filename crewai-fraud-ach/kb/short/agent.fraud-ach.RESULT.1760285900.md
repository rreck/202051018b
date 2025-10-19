```json
{
  "id": "1671851cfe16aba0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285900,
  "host_pid": "9e6742732c60:1",
  "hash": "d4add2b3c06b5b5d587b99cd007a90726fe98ebfa7509cc0234d885a9c375385",
  "cid": "QmV1d4add2b3c06b5b5d587b99cd007a90726fe98ebf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285900,
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
      "evaluated_at": 1760285900
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
  "sig": "893287f118e16d9b66de8e0711be16e0399271ff99cffaa05aa17fef3a268922"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}