```json
{
  "id": "b99339dd54833079",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286227,
  "host_pid": "9e6742732c60:1",
  "hash": "e8ea75cac49226a71b8aaba7d9bcd0f3e1c3c6a02a39c593497acf018f1cb1a6",
  "cid": "QmV1e8ea75cac49226a71b8aaba7d9bcd0f3e1c3c6a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286227,
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
      "evaluated_at": 1760286227
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
  "sig": "98f7749104c4bb8b131f75d0dedb80fb82b47e94c73f1be5f26236694a45cea4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}