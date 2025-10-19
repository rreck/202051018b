```json
{
  "id": "e0519140e345b4b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293921,
  "host_pid": "9e6742732c60:1",
  "hash": "29fead4c0413e4ede314f5fcda9dd543f588c1ebe00be1c664ce310e591ad510",
  "cid": "QmV129fead4c0413e4ede314f5fcda9dd543f588c1eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293921,
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
      "evaluated_at": 1760293921
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
  "sig": "43aa5592bdaee58ddfb01aad6a02241fa699a82146ef140b4d3fdfaa00cc5813"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153425339
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 100753656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'd6fcd27194bc1174'}}}