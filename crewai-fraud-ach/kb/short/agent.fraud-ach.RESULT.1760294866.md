```json
{
  "id": "da25042b361df5cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294866,
  "host_pid": "9e6742732c60:1",
  "hash": "2354124df14ea553ef458c004b99238e20e60697db1aec2570b20025ad6b0f99",
  "cid": "QmV12354124df14ea553ef458c004b99238e20e60697",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294866,
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
      "evaluated_at": 1760294866
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
  "sig": "613f68e2ec44322d0b35333b9f06423c2e8a57be07fa12bfce722b3c3746bca4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029709484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 100694688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'f2d4d1f000649e92'}}}