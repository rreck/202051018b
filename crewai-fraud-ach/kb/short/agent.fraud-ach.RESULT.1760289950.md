```json
{
  "id": "3553e6f851f2a0d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289950,
  "host_pid": "9e6742732c60:1",
  "hash": "ea6f5ae5d97430ac5b601a092a2cba605601f97ae64f7fcfbc3f563271621dba",
  "cid": "QmV1ea6f5ae5d97430ac5b601a092a2cba605601f97a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289950,
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
      "evaluated_at": 1760289950
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
  "sig": "1cfcb783ca721c5766232d2d9d6e6348b0929ec678034b4ac7983449480a3824"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 34077106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}