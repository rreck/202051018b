```json
{
  "id": "95ca3c7f10c9dbff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289769,
  "host_pid": "9e6742732c60:1",
  "hash": "7979f39fe1276164bf439711513f4a842df57e041aea66dcd49ed48cdc80f510",
  "cid": "QmV17979f39fe1276164bf439711513f4a842df57e04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289769,
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
      "evaluated_at": 1760289769
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
  "sig": "6de3ff33bf9f3499cb859df550a69a82ed630170a03eb062e14fb0f174922c06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 11098032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}