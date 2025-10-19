```json
{
  "id": "5117cdf2e118a251",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289532,
  "host_pid": "9e6742732c60:1",
  "hash": "27acb1e8c5fb3616e2fa7496153fc959c7e10eec6646debbc3eeaaa89c3a256e",
  "cid": "QmV127acb1e8c5fb3616e2fa7496153fc959c7e10eec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289532,
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
      "evaluated_at": 1760289532
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
  "sig": "7d563df21d55e728f0fd5a5a1274563cf7ee513f8897f11611851ef5c9cd922a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596329202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 21921480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': 'fa5bd443d3b1bd8d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}