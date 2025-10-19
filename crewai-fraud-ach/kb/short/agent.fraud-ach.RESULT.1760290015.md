```json
{
  "id": "7520b8a8285646f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290015,
  "host_pid": "9e6742732c60:1",
  "hash": "99577466c1a6675b14073ff2dfeac67345314af5b55d3962a94c3d6854ba1422",
  "cid": "QmV199577466c1a6675b14073ff2dfeac67345314af5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290015,
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
      "evaluated_at": 1760290015
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
  "sig": "e3caf5c52d88b7e4ce5cbb33a2e85cf7c7325829f07c3660e853a8a32808d7ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026466423
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 65639414, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': '1fcdc28f16166b10'}}}