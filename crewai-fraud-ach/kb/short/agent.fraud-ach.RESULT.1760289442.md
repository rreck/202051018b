```json
{
  "id": "6d66cd29fdbb16bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289442,
  "host_pid": "9e6742732c60:1",
  "hash": "36d968cf78b5e1f6bc8488f9a8656c47bc8e50a04f03ef073e4a4bec102a7557",
  "cid": "QmV136d968cf78b5e1f6bc8488f9a8656c47bc8e50a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289442,
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
      "evaluated_at": 1760289442
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
  "sig": "ad76355b842ab11fcf59c380b92d4238c6e6c62503d0a2eb51db4da60cf831b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 51349548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}