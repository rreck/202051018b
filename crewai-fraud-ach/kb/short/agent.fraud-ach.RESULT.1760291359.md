```json
{
  "id": "b308389af54a1965",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291359,
  "host_pid": "9e6742732c60:1",
  "hash": "731b43470e15c5d5bf7b87eb462b05f364887188eb93050bdc31803793583602",
  "cid": "QmV1731b43470e15c5d5bf7b87eb462b05f364887188",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291359,
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
      "evaluated_at": 1760291359
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
  "sig": "1aaa82e66087df8aa2d4da6d4e0b6d22003590ff97ca2a4a30d3b62bd99cd1a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023207579
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 62298684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '07d0951e15487e7b'}}}