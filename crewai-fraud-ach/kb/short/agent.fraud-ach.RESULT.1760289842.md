```json
{
  "id": "750bf5e638432a19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289842,
  "host_pid": "9e6742732c60:1",
  "hash": "cbea708f8b49c32d90cb5a9ba3badda78276e66e323f90d60039dc9abcbca7e5",
  "cid": "QmV1cbea708f8b49c32d90cb5a9ba3badda78276e66e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289842,
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
      "evaluated_at": 1760289842
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
  "sig": "1c6d12c33e6144038b8b3bb27ba68374b410a113ea9e20ed18697e133b1254c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 11266184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}