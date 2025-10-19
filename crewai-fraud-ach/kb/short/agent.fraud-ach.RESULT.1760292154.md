```json
{
  "id": "d04d35ffa4690430",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292154,
  "host_pid": "9e6742732c60:1",
  "hash": "963b6d8b86f1b5f29058ce5b1298203524d115156da989aa47b83c8c0dadf5c3",
  "cid": "QmV1963b6d8b86f1b5f29058ce5b1298203524d11515",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292154,
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
      "evaluated_at": 1760292154
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
  "sig": "b91d837f941bf6e65f6bf935a89ddd8fcc4cf097cdee0fb5a6063037c05b49c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 24297683, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}