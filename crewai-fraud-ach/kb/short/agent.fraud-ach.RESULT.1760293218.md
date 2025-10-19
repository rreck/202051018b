```json
{
  "id": "663eeaadae0ac12b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293218,
  "host_pid": "9e6742732c60:1",
  "hash": "2b12fbd41e4ac208d282b0b03471dc34b43385318789cf9dbe6226e30216f9aa",
  "cid": "QmV12b12fbd41e4ac208d282b0b03471dc34b4338531",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293218,
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
      "evaluated_at": 1760293218
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
  "sig": "0ed9da3615fc2f7887810b884bf9a91b6724e53f036d0ccd05076fccc6df3c71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596354415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 59563690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'f20df65cb297838c'}}}