```json
{
  "id": "b4fbe170c517ce78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294892,
  "host_pid": "9e6742732c60:1",
  "hash": "5c1b914703cbee2304af913c47f4f5de73841af613dd694fec1c9043ab2763cf",
  "cid": "QmV15c1b914703cbee2304af913c47f4f5de73841af6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294892,
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
      "evaluated_at": 1760294892
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
  "sig": "dd427c2e44692f0198b15d381046b7a60f5c5dc8d90427590649d4777a8be92e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021005824
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 12300000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '58a86144ce85b895'}}}