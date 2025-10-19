```json
{
  "id": "ea09ec37167fff6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290165,
  "host_pid": "9e6742732c60:1",
  "hash": "7575d969d427f0093427368cb0a1aa748617db74ec7382afd84f6a57871a1721",
  "cid": "QmV17575d969d427f0093427368cb0a1aa748617db74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290165,
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
      "evaluated_at": 1760290165
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
  "sig": "d6c139370b925ffd38d1a1d5f7efa8c6d3b1683a16376c8113aa166cbb0dd42f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 18256935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}