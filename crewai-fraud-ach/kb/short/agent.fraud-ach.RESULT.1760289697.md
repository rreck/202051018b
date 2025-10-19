```json
{
  "id": "b55b8bd2a67ec7a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289697,
  "host_pid": "9e6742732c60:1",
  "hash": "462fe923ab356399ff29cdc0f2727f3e77c8fc2d10f3b55da0b37822be158d99",
  "cid": "QmV1462fe923ab356399ff29cdc0f2727f3e77c8fc2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289697,
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
      "evaluated_at": 1760289697
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
  "sig": "efd2df043d8f7300c727e680ee3fe7e4e6113191bcc560b7b1711399bb0ab513"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 14845740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}