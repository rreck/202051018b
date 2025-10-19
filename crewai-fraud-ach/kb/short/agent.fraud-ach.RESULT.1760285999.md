```json
{
  "id": "af2bd17cc85dd597",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285999,
  "host_pid": "9e6742732c60:1",
  "hash": "c8a9c4d0d684f55d2046140a7487737a0a5baa5a543ad1d77f053a68375e41c4",
  "cid": "QmV1c8a9c4d0d684f55d2046140a7487737a0a5baa5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285999,
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
      "evaluated_at": 1760285999
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
  "sig": "7732f95d0cd7c23b669425749b0313c2d376d51467ca6f0e57c9d5fe4cf5b550"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201461662622
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}