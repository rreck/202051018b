```json
{
  "id": "690588bf4aa1e6ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287520,
  "host_pid": "9e6742732c60:1",
  "hash": "878f14508953d1a8d227982fd4f2dbb8fb1e40a9ebd8141c68f6524df2bc827a",
  "cid": "QmV1878f14508953d1a8d227982fd4f2dbb8fb1e40a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287520,
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
      "evaluated_at": 1760287520
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
  "sig": "b0efcaa90c0c01787e1933516440234ce0ad3279f57e0bf17ceeb1799224c5e4"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 18776142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}