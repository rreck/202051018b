```json
{
  "id": "6d87128676be75d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291824,
  "host_pid": "9e6742732c60:1",
  "hash": "c779f15c5286d717b9c2754182bed2ba41bf3fa3154594eb5b1bc475fa054a2e",
  "cid": "QmV1c779f15c5286d717b9c2754182bed2ba41bf3fa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291824,
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
      "evaluated_at": 1760291824
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
  "sig": "b389eb4edd09cd0ecde0a9aceb595484736a9a792bfaf491db3eee295900e0f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244433200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 27365216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'e1a08016c5f05bd5'}}}