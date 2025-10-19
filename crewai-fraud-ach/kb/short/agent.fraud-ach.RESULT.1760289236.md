```json
{
  "id": "5909491ed324656b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289236,
  "host_pid": "9e6742732c60:1",
  "hash": "d7bc6596eabd193a24f07b820369c0d8dce4398f7550a56a0324b1da9c3bcf19",
  "cid": "QmV1d7bc6596eabd193a24f07b820369c0d8dce4398f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289236,
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
      "evaluated_at": 1760289236
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
  "sig": "12fcc1b449478ea300a78d9b1d5fb8964baf51f70b2d0b19169151802ca003fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 53678313, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}