```json
{
  "id": "cb57aeb00cf5dff0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289719,
  "host_pid": "9e6742732c60:1",
  "hash": "971c2785f7c506024a5304d43e6f4b71baab8ee7ab6000492c4aa0157c7428f8",
  "cid": "QmV1971c2785f7c506024a5304d43e6f4b71baab8ee7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289719,
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
      "evaluated_at": 1760289719
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
  "sig": "2c37b9de8f5fe9c8f63eea5b299361dcea04eeaf10e6a60aef177e899c588246"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027363246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 15177136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}