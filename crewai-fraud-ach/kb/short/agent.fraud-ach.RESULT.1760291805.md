```json
{
  "id": "23630544adbb4693",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291805,
  "host_pid": "9e6742732c60:1",
  "hash": "22f6ef114fc254102df087b64d01713b96479d1114d8be8b1d5749725c7bf573",
  "cid": "QmV122f6ef114fc254102df087b64d01713b96479d11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291805,
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
      "evaluated_at": 1760291805
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
  "sig": "2ed8d77970c2a7c97dd1ad0b6610cd089104423a259e16f516855985092bb1a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022605707
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 50473962, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '50e001b692c48bf8'}}}