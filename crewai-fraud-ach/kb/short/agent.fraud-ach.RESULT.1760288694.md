```json
{
  "id": "49ae8a25445f023b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288694,
  "host_pid": "9e6742732c60:1",
  "hash": "ae8b91fed11af1a5d79065f05092b54d2b5cfb533c3470c9b868fe7dedf142a0",
  "cid": "QmV1ae8b91fed11af1a5d79065f05092b54d2b5cfb53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288694,
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
      "evaluated_at": 1760288694
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
  "sig": "50d1daa6763af77f728a93d41b8373abd282e457de6f5d38b3522fcc0bbc8afe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 10727816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}