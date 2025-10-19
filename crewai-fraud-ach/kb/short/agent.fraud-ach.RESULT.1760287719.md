```json
{
  "id": "9660175270a07b0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287719,
  "host_pid": "9e6742732c60:1",
  "hash": "7fa390e7cde51a7497e61301dcfa0e7abdf7b0f3fb4bd4f221022389fa883224",
  "cid": "QmV17fa390e7cde51a7497e61301dcfa0e7abdf7b0f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287719,
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
      "evaluated_at": 1760287719
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
  "sig": "302e9356eeae32b2345aec3efb0e45b83fce618ddd8b36edeac8ea0c8f95ce9d"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 031201462273667
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 31254090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285763, 'matching_hash': 'db56bbc4ded669a9'}}}