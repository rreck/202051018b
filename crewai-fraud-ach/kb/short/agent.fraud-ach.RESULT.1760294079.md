```json
{
  "id": "0b7b3cdd95134c4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294079,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce13d870ce3581724039d08282c43a7dc5a33339fc081b2959748aaca039d06",
  "cid": "QmV18ce13d870ce3581724039d08282c43a7dc5a3333",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294079,
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
      "evaluated_at": 1760294079
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
  "sig": "b667f208c3a328b971c1ba8b37545ec177651e5666a2a3657213a3ce6aecb047"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 13654179, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}