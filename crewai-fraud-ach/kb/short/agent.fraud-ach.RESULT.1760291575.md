```json
{
  "id": "951c60d7c4ff09ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291575,
  "host_pid": "9e6742732c60:1",
  "hash": "4b59651d300aec0d124268c44fb8f68d1c5d801fa86eb6b43dd1907acde7f1c1",
  "cid": "QmV14b59651d300aec0d124268c44fb8f68d1c5d801f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291575,
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
      "evaluated_at": 1760291575
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
  "sig": "07759c86cc7d94a5d21a2690da49320e7fb12886d4ce02b6932de211d9dece27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592616863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 17063258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '1f69fcd8882944a6'}}}