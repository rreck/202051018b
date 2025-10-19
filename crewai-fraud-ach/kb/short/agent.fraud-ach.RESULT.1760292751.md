```json
{
  "id": "388371c986575c0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292751,
  "host_pid": "9e6742732c60:1",
  "hash": "a2547a6d82e1cb6fbc491f84e2f611486a2ea30b0e4dcb9f2941dc4a7ff4923a",
  "cid": "QmV1a2547a6d82e1cb6fbc491f84e2f611486a2ea30b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292751,
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
      "evaluated_at": 1760292751
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
  "sig": "920bbd731033cfc40e33f5539cb2719df27b15d7776c1381c542b6503e054374"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596790322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 280, 'threshold': 50, 'total_amount': 14653520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 279, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}