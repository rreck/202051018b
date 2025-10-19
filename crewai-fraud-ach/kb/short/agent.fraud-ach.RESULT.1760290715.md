```json
{
  "id": "7108868dfdea51ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290715,
  "host_pid": "9e6742732c60:1",
  "hash": "240318751d9451c426ca4c4035e907fceecafbdcb999c9ebb9c2d46e26629272",
  "cid": "QmV1240318751d9451c426ca4c4035e907fceecafbdc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290715,
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
      "evaluated_at": 1760290715
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
  "sig": "7293a9b5c4af94ca046476fe0969c54b56c36e9f8b6048ae3a52fdb4d235e0d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240022849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 52351964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}