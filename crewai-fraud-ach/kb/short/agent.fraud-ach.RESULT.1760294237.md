```json
{
  "id": "70d1d55d0654d9a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294237,
  "host_pid": "9e6742732c60:1",
  "hash": "6f4133493145449d46615464a91779cf4c3766c31de961622aaaa5a2752b0d0d",
  "cid": "QmV16f4133493145449d46615464a91779cf4c3766c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294237,
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
      "evaluated_at": 1760294237
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
  "sig": "6151e3862c4a4d49841972ab4000b0110638be7472789cf5d4707922aa961c22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 95874012, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}