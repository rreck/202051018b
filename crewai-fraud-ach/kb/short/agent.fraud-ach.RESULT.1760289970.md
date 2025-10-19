```json
{
  "id": "ef41f86f4c3b1fa3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289970,
  "host_pid": "9e6742732c60:1",
  "hash": "30e09405003d72d2b68c9263916b5aca678a55910043ae6569c0920d8b342353",
  "cid": "QmV130e09405003d72d2b68c9263916b5aca678a5591",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289970,
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
      "evaluated_at": 1760289970
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
  "sig": "fe151493bbe927a7a18fd76560d01f51b1d22ed67a4aa587827c7fc311192041"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 36786660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}