```json
{
  "id": "5c40044ad5bcc779",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294198,
  "host_pid": "9e6742732c60:1",
  "hash": "124fbfe8c8fe45389cac0c3b0cdcc2113dc9442b74b6d7bd6bb141b3f8a2f26c",
  "cid": "QmV1124fbfe8c8fe45389cac0c3b0cdcc2113dc9442b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294198,
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
      "evaluated_at": 1760294198
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
  "sig": "38378cf3099f5278ee5b64a0c6ff09206c04f989569416e0020328617681900b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 74303933, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}