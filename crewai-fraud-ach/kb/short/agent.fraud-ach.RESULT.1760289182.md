```json
{
  "id": "48101fd35a83bfd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289182,
  "host_pid": "9e6742732c60:1",
  "hash": "f7d77199932245c98933aed76475c02df5518dee6a00a51f3dd76142e5ccdec9",
  "cid": "QmV1f7d77199932245c98933aed76475c02df5518dee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289182,
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
      "evaluated_at": 1760289182
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
  "sig": "1e0fa08c95d59bd26c26a897d738a077fae510573cd09aa6df838f138dca3ee8"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 063100279773830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 58000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '49e9eab15cee1f0f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}