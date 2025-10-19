```json
{
  "id": "8e70ac8eb15291fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290081,
  "host_pid": "9e6742732c60:1",
  "hash": "eb0e6414aa9e39bda02866aa89d731e6f20764e57c9a66fdaedabcc664198d0b",
  "cid": "QmV1eb0e6414aa9e39bda02866aa89d731e6f20764e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290081,
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
      "evaluated_at": 1760290081
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
  "sig": "30704a6328e6de082604251154bac48ef968b574672f4f234230a7d491e7e947"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027732309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 25240410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '37acd6c3ead193e2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}