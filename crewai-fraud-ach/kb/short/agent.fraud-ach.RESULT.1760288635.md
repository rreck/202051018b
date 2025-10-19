```json
{
  "id": "72a26ec884238895",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288635,
  "host_pid": "9e6742732c60:1",
  "hash": "9b66630cff8149b107f57821cc37e1e6c82ca99504aa2a6e600fb56c428aa611",
  "cid": "QmV19b66630cff8149b107f57821cc37e1e6c82ca995",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288635,
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
      "evaluated_at": 1760288635
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
  "sig": "8958e8853d55d8791b181b8d1961001fd5dc5a03107408bc3a21b8cad3a4dcfa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 15974343, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}