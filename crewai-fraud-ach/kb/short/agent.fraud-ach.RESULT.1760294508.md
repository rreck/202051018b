```json
{
  "id": "9ff1cccbe5306091",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294508,
  "host_pid": "9e6742732c60:1",
  "hash": "0390e6da92423420749437f1be70f804c1b6242c9e305fbc491d7008a6e00c1a",
  "cid": "QmV10390e6da92423420749437f1be70f804c1b6242c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294508,
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
      "evaluated_at": 1760294508
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
  "sig": "58748d2b30c954f698e948ffe0faff5ca8ef161686b9ce2a143d079bda29a59b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 62472927, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '880809095', 'validation_error': 'Invalid routing number checksum'}}}