```json
{
  "id": "5d965475790b1072",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286505,
  "host_pid": "9e6742732c60:1",
  "hash": "8d8d275575f23bc4dbe1005c1ab55e2f5451559ef40815aed02d1166e878d8d5",
  "cid": "QmV18d8d275575f23bc4dbe1005c1ab55e2f5451559e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286505,
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
      "evaluated_at": 1760286505
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
  "sig": "767adf3228632cd64da4806c97753ecdc2161854c34ea58ee8acb7e84677b373"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153543170
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}