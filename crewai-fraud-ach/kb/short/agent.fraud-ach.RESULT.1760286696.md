```json
{
  "id": "576101ad74f065be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286696,
  "host_pid": "9e6742732c60:1",
  "hash": "4ba51631e8636e179dae615c26bbdd8036a1dbba4f6f6b1a937b15c464648f61",
  "cid": "QmV14ba51631e8636e179dae615c26bbdd8036a1dbba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286696,
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
      "evaluated_at": 1760286696
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "55a4e18d64775abf58f44420008fd8e3681d2915963654e4ba7a7d66271e66b7"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000035326391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12705732, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '7c05ec5f373172f0'}}}