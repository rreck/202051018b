```json
{
  "id": "d44d021f60f84359",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286668,
  "host_pid": "9e6742732c60:1",
  "hash": "1e677bc83d32b4ff0504622d5f17d5f0cff7957ab458d519f6b5e852fba8329d",
  "cid": "QmV11e677bc83d32b4ff0504622d5f17d5f0cff7957a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286668,
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
      "evaluated_at": 1760286668
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
  "sig": "3547ec08b040b459420781f180bd33b8b378d61d762e6fc6495e83c9e189ca86"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026169646
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285763, 'matching_hash': 'b8e6d176a4768585'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}