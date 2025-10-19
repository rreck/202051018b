```json
{
  "id": "999bbef9ed9e8dba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293737,
  "host_pid": "9e6742732c60:1",
  "hash": "e834f4665a00611cf12d29b0b3fbfa5ba04cc6399d6b79d6c8e62cb0c1f0672e",
  "cid": "QmV1e834f4665a00611cf12d29b0b3fbfa5ba04cc639",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293737,
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
      "evaluated_at": 1760293737
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
  "sig": "4080fc882e9aef95f91985970d6bd57a494974ee6eddb40f4437bebe5bb01330"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 22673728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}