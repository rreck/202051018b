```json
{
  "id": "27575a239113a25c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292379,
  "host_pid": "9e6742732c60:1",
  "hash": "56b531606db5b8bd29211fd8ef1a951e18cbc8f38a9e2b1493c30bcf58d00cce",
  "cid": "QmV156b531606db5b8bd29211fd8ef1a951e18cbc8f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292379,
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
      "evaluated_at": 1760292379
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
  "sig": "7b757718c8c937930ec5a20174c567b2a36995271e65b7fa43de923986801cd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461436182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 26400024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': 'd641045bf224534b'}}}