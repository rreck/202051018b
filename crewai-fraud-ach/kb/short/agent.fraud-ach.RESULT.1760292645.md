```json
{
  "id": "c6dd47de30e0e58f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292645,
  "host_pid": "9e6742732c60:1",
  "hash": "3c11559d003431fb2d60143136bb82671c2b83586a91477cc3a4a281d87eb518",
  "cid": "QmV13c11559d003431fb2d60143136bb82671c2b8358",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292645,
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
      "evaluated_at": 1760292645
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "e1cf45dbdf704b77c47de922025fb5378bca5d366d6a4ed3887514806829d0a1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 79546186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}