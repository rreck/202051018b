```json
{
  "id": "faaf3210910e68fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291579,
  "host_pid": "9e6742732c60:1",
  "hash": "b3276bc18bab30950ce8fb474fc32e24ba6e504a2e3b18e1e6954712cf89980c",
  "cid": "QmV1b3276bc18bab30950ce8fb474fc32e24ba6e504a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291579,
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
      "evaluated_at": 1760291579
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
  "sig": "b1cb6c74ccc1da11e2c3bc463d93c389222fb82a1dc412fb24c1c187c88bef86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467395210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 19865868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': 'b5e2565aea18e07c'}}}