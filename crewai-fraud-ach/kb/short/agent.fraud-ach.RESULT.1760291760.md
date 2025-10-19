```json
{
  "id": "7f1690033ed062a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291760,
  "host_pid": "9e6742732c60:1",
  "hash": "d261b0507e1ebb4a0654e386322ab5db2158baa2aeda582a1ee406403d41df9f",
  "cid": "QmV1d261b0507e1ebb4a0654e386322ab5db2158baa2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291760,
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
      "evaluated_at": 1760291760
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
  "sig": "2d7cf1210ca61c283a828fb7334eeac3ac582fa2973f448b3e2e7fcbff556dbb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023386962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 18200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}