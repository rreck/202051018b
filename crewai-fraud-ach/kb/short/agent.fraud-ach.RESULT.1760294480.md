```json
{
  "id": "d4823b76b8696342",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294480,
  "host_pid": "9e6742732c60:1",
  "hash": "8940f9211d19792b89c8b663bfbf652669488f1a6b510624bf14b2ef03ab64e3",
  "cid": "QmV18940f9211d19792b89c8b663bfbf652669488f1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294480,
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
      "evaluated_at": 1760294480
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "d1f482794cc464d85dfdcb259084fee6f24deb908aeedd9c2072b742b6d144a8"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467541453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 119500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '2d82340c3dc0e840'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}