```json
{
  "id": "3f925bf224cbfc2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291331,
  "host_pid": "9e6742732c60:1",
  "hash": "a80ae17cd51d25409c8c2708338f0293851a76bfacca4dc1686ebedea7f8fcda",
  "cid": "QmV1a80ae17cd51d25409c8c2708338f0293851a76bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291331,
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
      "evaluated_at": 1760291331
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "3883d7a8276c5230e5c883a1b5df12728f72efac0f869509148cca3241fd02bc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 58244188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}