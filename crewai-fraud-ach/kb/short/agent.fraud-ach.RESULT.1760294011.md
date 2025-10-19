```json
{
  "id": "ca39e6b4c81a28e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294011,
  "host_pid": "9e6742732c60:1",
  "hash": "c8e0b59a5d48aa7fa11b6d207d06df0d23d2865872d1cc652e1c11c5ff6cb688",
  "cid": "QmV1c8e0b59a5d48aa7fa11b6d207d06df0d23d28658",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294011,
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
      "evaluated_at": 1760294011
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
  "sig": "7be78abfe35d0e3b3767508430e7dfedff220cc3b5e0a220472e126f68daab20"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000241606573
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 115000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '2fa99cb8a6f007e0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}