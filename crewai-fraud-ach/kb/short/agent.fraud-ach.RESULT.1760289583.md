```json
{
  "id": "41827716bc55a53d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289583,
  "host_pid": "9e6742732c60:1",
  "hash": "5f85e1d0e4e62bf2fd1f908b0ab0476d9113306061955237a55336c3eec73953",
  "cid": "QmV15f85e1d0e4e62bf2fd1f908b0ab0476d91133060",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289583,
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
      "evaluated_at": 1760289583
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
  "sig": "68ddf8f486a4150b04e95769cbed4162d951dfcc1b4f8494491e47d86a9bf6dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270344488
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 33877631, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}