```json
{
  "id": "4bac4438a16552d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286621,
  "host_pid": "9e6742732c60:1",
  "hash": "9857576fbe48d1067559c89ad0b2ebfa3b57a29cb046246d6be54a2855f71588",
  "cid": "QmV19857576fbe48d1067559c89ad0b2ebfa3b57a29c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286621,
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
      "evaluated_at": 1760286621
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
  "sig": "69df96e4f77d37ab913a9cb5609fd6b467f0fb5348a9df35e3d24d6768828318"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105158642736
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': '1f64147e0a165b3c'}}}