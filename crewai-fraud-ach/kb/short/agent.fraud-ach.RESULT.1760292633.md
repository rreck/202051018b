```json
{
  "id": "822711847d129963",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292633,
  "host_pid": "9e6742732c60:1",
  "hash": "986214f0768a820da8e88d23612d9919e05cacd8a6f96cbe335a6bebe46fb4e3",
  "cid": "QmV1986214f0768a820da8e88d23612d9919e05cacd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292633,
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
      "evaluated_at": 1760292633
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
  "sig": "b34d6166e88bda6a6ab02e5093bcf7fadd531a7a85e9fe521f284d0babfbe32d"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 063100279773830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 101000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '49e9eab15cee1f0f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}outing number checksum'}}}