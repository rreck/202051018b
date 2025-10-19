```json
{
  "id": "3c7b7337f4e27d53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288055,
  "host_pid": "9e6742732c60:1",
  "hash": "c45ac7297075de6cdc4a34a79f7066ded8f06454bc0268273cfbcb048d90197d",
  "cid": "QmV1c45ac7297075de6cdc4a34a79f7066ded8f06454",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288055,
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
      "evaluated_at": 1760288055
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
  "sig": "20c894f601d9cc1c520275b2b07400a79b99dfe76665d7602e1ae4b1b6d0365a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596811195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 17863983, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': '0f37bc2cbfa5aec6'}}}}}fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}