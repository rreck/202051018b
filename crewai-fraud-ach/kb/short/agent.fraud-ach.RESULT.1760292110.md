```json
{
  "id": "e3e3758c8aa9ff1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292110,
  "host_pid": "9e6742732c60:1",
  "hash": "8cbfdb5d018e9e825832f74a8ac9c7b2e7ef22ffdb9a0c486434c0a78f9d65c5",
  "cid": "QmV18cbfdb5d018e9e825832f74a8ac9c7b2e7ef22ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292110,
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
      "evaluated_at": 1760292110
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
  "sig": "7656e68b38842a5c1c2f2c7bbacc2d481f811aa6872a06bd9808dcf1a9356129"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 21617820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}