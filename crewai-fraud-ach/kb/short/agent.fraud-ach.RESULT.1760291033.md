```json
{
  "id": "d3af35f7c8d11506",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291033,
  "host_pid": "9e6742732c60:1",
  "hash": "852eb97ccc2bc0bde994a52d87bb4d6febcf0d09543b442565da4e291c195201",
  "cid": "QmV1852eb97ccc2bc0bde994a52d87bb4d6febcf0d09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291033,
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
      "evaluated_at": 1760291033
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
  "sig": "61e6b84e4ec0ff6c049d2045b8ff51d21125689dd928230b9e686cc834b460cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244947778
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 48969525, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}